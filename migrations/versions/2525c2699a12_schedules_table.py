"""schedules table

Revision ID: 2525c2699a12
Revises: 0daafad551b9
Create Date: 2023-03-18 08:47:11.502379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2525c2699a12'
down_revision = '0daafad551b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('adresse', sa.String(length=255), nullable=True),
    sa.Column('appartment', sa.String(length=64), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_schedule_adresse'), ['adresse'], unique=False)
        batch_op.create_index(batch_op.f('ix_schedule_appartment'), ['appartment'], unique=False)
        batch_op.create_index(batch_op.f('ix_schedule_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_schedule_notes'), ['notes'], unique=False)
        batch_op.create_index(batch_op.f('ix_schedule_status'), ['status'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_schedule_status'))
        batch_op.drop_index(batch_op.f('ix_schedule_notes'))
        batch_op.drop_index(batch_op.f('ix_schedule_date'))
        batch_op.drop_index(batch_op.f('ix_schedule_appartment'))
        batch_op.drop_index(batch_op.f('ix_schedule_adresse'))

    op.drop_table('schedule')
    # ### end Alembic commands ###